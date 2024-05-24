"""
Essa é a main do bot, onde o bot é instanciado, a factory do instagram_manager é instanciada,
o instagram_manager é instanciado e o bot é iniciado. Dessa forma, para adicionar um novo
instagram_manager, basta criar uma nova classe que implemente a interface IInstagramManager
e adicionar na factory. Irá receber uma instância dos models para poder alterar o estado
da aplicação e refletir na interface gráfica.
"""
import random
import time
from time import sleep

from src.clients.actions_client import ActionsClient
from src.gui.models.config_model import ConfigModel
from src.gui.models.groups_model import GroupsModel
from src.interfaces.i_manager import IManager


class Bot:
    def __init__(
        self,
        manager: IManager,
        groups_model: GroupsModel,
        config_model: ConfigModel,
        actions_client: ActionsClient,
        group_index: int,
    ) -> None:
        self.manager = manager
        self.groups_model = groups_model
        self.config_model = config_model
        self.actions_client = actions_client
        self.group_index = group_index

    def start(self) -> None:
        self.update_log('Verificando se todas as contas tão logadas...')
        profiles = self.groups_model.get_group_profiles_info_list(
            self.group_index
        )

        self.manager.prepare()

        if self.manager.is_no_account_logged():
            self.update_log('Nenhuma conta logada, entrando em todas...')
            logged_accounts = self.login_all(profiles)

        else:
            already_logged = self.manager.get_logged_accounts()

            self.update_log(f"Contas logadas: {', '.join(already_logged)}")

            accounts_to_logout = self.get_accounts_to_logout(
                profiles, already_logged
            )
            accounts_to_login = self.get_accounts_to_login(
                profiles, already_logged
            )
            logged_accounts = list(
                set(already_logged) - set(accounts_to_logout)
            )

            if accounts_to_logout:
                self.logout(accounts_to_logout)

            logged_accounts = [
                *logged_accounts,
                *self.login_all(accounts_to_login),
            ]

        self.update_log(
            'Todas as contas logadas, iniciando a execução do bot...'
        )

        actions_done = 0
        actions_done_per_account = {account: 0 for account in logged_accounts}
        actions_to_do = self.config_model.actions_goal
        actions_to_switch_account = self.config_model.actions_to_switch_account
        switch_account_with_no_tasks = (
            self.config_model.switch_account_with_no_tasks
        )
        time_without_tasks_to_wait = (
            self.config_model.time_without_tasks_to_wait
        )
        time_to_wait_min = self.config_model.time_between_actions_min
        time_to_wait_max = self.config_model.time_between_actions_max

        for account in logged_accounts:
            self.actions_client.add_profile(
                account,
                [
                    profile['password']
                    for profile in profiles
                    if profile['username'] == account
                ][0],
            )

        while actions_done < actions_to_do:
            for account in logged_accounts:

                self.manager._restart_app()

                self.groups_model.set_group_current_account(
                    self.group_index, account
                )
                self.update_log(f'Executando ações na conta {account}...')
                self.manager.change_to_account(account)

                while (
                    actions_done_per_account[account]
                    % actions_to_switch_account
                    != 0
                    or actions_done_per_account[account] == 0
                ):

                    if actions_done >= actions_to_do:
                        self.update_log(
                            'Meta de ações atingida, finalizando execução...'
                        )
                        return

                    if switch_account_with_no_tasks:
                        self.update_log(
                            f'Esperando ação para a conta {account} por até {time_without_tasks_to_wait} segundos...'
                        )
                        action = self.wait_for_action(
                            account, time_without_tasks_to_wait
                        )
                        if not action:
                            break
                    else:
                        self.update_log(
                            f'Esperando ação para a conta {account} até encontrar...'
                        )
                        action = self.get_action(account)

                    order = action['order']
                    link = action['link']
                    short_link = action['shortcode']
                    comment = action['comment']
                    comment_id = action['commentId']

                    self.update_log(
                        f'Comentando no post {short_link} com a conta {account}...'
                    )
                    result = self.manager.comment(link, comment)
                    if result:
                        self.update_log(f'Comentário realizado com sucesso!')
                        self.actions_client.confirm_action(
                            account, order, comment_id
                        )
                        actions_done += 1
                        actions_done_per_account[account] += 1
                        self.update_profile_actions_done(
                            account, actions_done_per_account[account]
                        )

                    time_to_wait = random.randint(
                        time_to_wait_min, time_to_wait_max
                    )
                    self.update_log(
                        f'Esperando {time_to_wait} segundos para a próxima ação...'
                    )
                    sleep(time_to_wait)

    def update_profile_actions_done(
        self, account: str, actions_done: int
    ) -> None:
        self.groups_model.edit_group_profile_actions_done(
            self.group_index, account, 0, 0, actions_done
        )

    def get_action(self, account: str) -> dict:
        while True:
            action = self.actions_client.get_action(account)
            if 'error' not in action.keys():
                break

    def wait_for_action(self, account: str, time_to_wait: int) -> None:
        actual_time = time.time()

        while time.time() - actual_time < time_to_wait:
            action = self.actions_client.get_action(account)
            if 'error' not in action.keys():
                break

        if 'error' in action.keys():
            return False

        return action

    def logout(self, accounts_to_logout: list) -> None:
        for account in accounts_to_logout:
            self.manager.logout()
            self.update_log(f'Conta {account} deslogada.')

    def login_all(self, accounts_to_login: list) -> list:
        logged_accounts = []
        for account in accounts_to_login:
            self.update_log(f"Logando na conta {account['username']}...")

            username = account['username']
            password = account['password']

            self.manager.add_new_account()

            if self.manager.login(username, password):
                self.update_log(f'Conta {username} logada.')
                logged_accounts.append(username)
            else:
                self.update_log(f'Erro ao logar na conta {username}.')
        return logged_accounts

    def get_accounts_to_login(
        self, profiles: list, logged_accounts: list
    ) -> list:
        accounts_to_login = []
        for profile in profiles:
            if profile['username'] not in logged_accounts:
                accounts_to_login.append(profile)

        return accounts_to_login

    def get_accounts_to_logout(
        self, profiles: list, logged_accounts: list
    ) -> list:
        accounts_to_logout = set(logged_accounts) - set(
            [profile['username'] for profile in profiles]
        )
        return accounts_to_logout

    def update_log(self, message: str) -> None:
        self.groups_model.edit_group_current_log(self.group_index, message)
        sleep(2)
