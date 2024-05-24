from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.controllers.groups_controller import GroupsController
from src.gui.controllers.start_controller import StartController
from src.gui.resources.group_view_rc import GroupGUI
from src.gui.views.edit_profile_view import EditProfileView
from src.gui.workers.start_worker import StartWorker


class GroupView(GroupGUI, QMainWindow):
    def __init__(
        self,
        edit_profile_view: EditProfileView,
        groups_controller: GroupsController,
        start_controller: StartController,
        group_index: int,
        parent=None,
    ) -> None:
        super(GroupView, self).__init__(parent)
        self.setupUi(self)
        self._edit_profile_view = edit_profile_view
        self._groups_controller = groups_controller
        self._start_controller = start_controller
        self._group_index = group_index

        self._groups_controller.profile_added.connect(
            self.create_profile_frame
        )
        self._groups_controller.profile_removed.connect(
            self.remove_profile_frame
        )
        self._groups_controller.profile_edited.connect(self.edit_profile_frame)
        self._groups_controller.group_edited.connect(self.on_group_edited)
        self._groups_controller.current_account_changed.connect(
            self.on_current_account_changed
        )

        self.label_current_log.setText('Aguardando início...')
        self.frame_33.hide()   # temporário
        self.add_initial_profiles()

        self.start_worker = StartWorker(self._start_controller)
        self.button_start_all.clicked.connect(self.start_bot)

    def on_current_account_changed(
        self, group_index: int, username: str
    ) -> None:
        if group_index == self._group_index:
            self._set_all_current_account_labels_to_empty()
            label_current_account = self.findChild(
                QtWidgets.QLabel, 'label_current_account_' + username
            )
            label_current_account.setText('=>')

    def _set_all_current_account_labels_to_empty(self) -> None:
        for group_info in self._groups_controller.get_groups_info():
            if group_info.get('index') == self._group_index:
                for profile in group_info.get('profiles', []):
                    label_current_account = self.findChild(
                        QtWidgets.QLabel,
                        'label_current_account_' + profile.get('username'),
                    )
                    label_current_account.setText('')

    def on_group_edited(self, group_info: dict) -> None:
        if group_info.get('index') == self._group_index:
            self.label_current_log.setText(group_info.get('current_log'))

    def start_bot(self) -> None:
        self.start_worker.group_index = self._group_index
        self.start_worker.start()

    def show_popup(self, title: str, text: str) -> None:
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def add_initial_profiles(self) -> None:
        group_info = self._groups_controller.get_group_info(self._group_index)
        profiles = group_info.get('profiles', [])
        for profile in profiles:
            self.create_profile_frame(profile)

    def edit_profile_frame(self, old_username: str, profile: dict) -> None:
        new_username = profile.get('username')
        if old_username != new_username:
            self.remove_profile_frame(old_username)
            self.create_profile_frame(profile)
        else:
            profile_frame = self.findChild(
                QtWidgets.QFrame, 'profile_frame_' + new_username
            )
            label_actions_done = profile_frame.findChild(
                QtWidgets.QLabel, 'label_actions_done_' + new_username
            )
            label_actions_done.setText(
                f"{profile.get('like_actions_done')}           {profile.get('follow_actions_done')}           {profile.get('comment_actions_done')}"
            )

    def create_profile_frame(self, profile: dict) -> None:

        username = profile.get('username')
        like_actions_done = profile.get('like_actions_done')
        follow_actions_done = profile.get('follow_actions_done')
        comment_actions_done = profile.get('comment_actions_done')

        profile_frame = QtWidgets.QFrame(self.frame_32)
        profile_frame.setMinimumSize(QtCore.QSize(0, 40))
        profile_frame.setStyleSheet('')
        profile_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        profile_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        profile_frame.setObjectName('profile_frame_' + username)

        horizontal_layout = QtWidgets.QHBoxLayout(profile_frame)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setObjectName('horizontalLayout_' + username)

        frame_username = QtWidgets.QFrame(profile_frame)
        frame_username.setMaximumSize(QtCore.QSize(150, 16777215))
        frame_username.setStyleSheet('')
        frame_username.setFrameShape(QtWidgets.QFrame.NoFrame)
        frame_username.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_username.setObjectName('frame_username_' + username)

        horizontal_layout2 = QtWidgets.QHBoxLayout(frame_username)
        horizontal_layout2.setObjectName('horizontalLayout2_' + username)

        label_current_account = QtWidgets.QLabel(frame_username)
        label_current_account.setMaximumSize(QtCore.QSize(15, 16777215))
        label_current_account.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_current_account.setObjectName(
            'label_current_account_' + username
        )
        horizontal_layout2.addWidget(label_current_account)

        label_username = QtWidgets.QLabel(frame_username)
        label_username.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_username.setAlignment(QtCore.Qt.AlignCenter)
        label_username.setObjectName('label_username_' + username)
        label_username.setText('@' + username)
        horizontal_layout2.addWidget(label_username)

        horizontal_layout.addWidget(frame_username)

        frame_actions_done = QtWidgets.QFrame(profile_frame)
        frame_actions_done.setMinimumSize(QtCore.QSize(236, 0))
        frame_actions_done.setMaximumSize(QtCore.QSize(236, 16777215))
        frame_actions_done.setStyleSheet('')
        frame_actions_done.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_actions_done.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_actions_done.setObjectName('frame_actions_done_' + username)

        vertical_layout = QtWidgets.QVBoxLayout(frame_actions_done)
        vertical_layout.setObjectName('verticalLayout_' + username)

        label_actions_done = QtWidgets.QLabel(frame_actions_done)
        label_actions_done.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_actions_done.setAlignment(QtCore.Qt.AlignCenter)
        label_actions_done.setObjectName('label_actions_done_' + username)
        label_actions_done.setText(
            f'{like_actions_done}           {follow_actions_done}           {comment_actions_done}'
        )

        vertical_layout.addWidget(label_actions_done)
        horizontal_layout.addWidget(frame_actions_done)

        frame_other_actions = QtWidgets.QFrame(profile_frame)
        frame_other_actions.setMinimumSize(QtCore.QSize(20, 0))
        frame_other_actions.setStyleSheet('border: 0px;')
        frame_other_actions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_other_actions.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_other_actions.setObjectName('frame_other_actions_' + username)

        vertical_layout_2 = QtWidgets.QVBoxLayout(frame_other_actions)
        vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        vertical_layout_2.setSpacing(0)
        vertical_layout_2.setObjectName('verticalLayout2_' + username)

        button_other_actions = QtWidgets.QPushButton(frame_other_actions)
        button_other_actions.setMinimumSize(QtCore.QSize(18, 18))
        button_other_actions.setMaximumSize(QtCore.QSize(18, 16777215))
        button_other_actions.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        button_other_actions.setStyleSheet(
            'background-image: url(:/imagens/imagens/more_resized.png);'
        )
        button_other_actions.setText('')
        button_other_actions.setObjectName('button_other_actions_' + username)

        menu = QtWidgets.QMenu()
        menu.addAction(
            'Excluir perfil',
            lambda: self._groups_controller.remove_profile_from_group(
                self._group_index, username
            ),
        )
        menu.addAction(
            'Ver informações',
            lambda: self.show_popup(
                'Informações', self.get_profile_info_string(username)
            ),
        )
        menu.addAction(
            'Editar perfil', lambda: self.open_edit_profile_view(profile)
        )

        button_other_actions.setMenu(menu)

        vertical_layout_2.addWidget(button_other_actions)
        horizontal_layout.addWidget(
            frame_other_actions, 0, QtCore.Qt.AlignCenter
        )

        self.verticalLayout_26.addWidget(profile_frame)

    def remove_profile_frame(self, username: str) -> None:
        profile_frame = self.findChild(
            QtWidgets.QFrame, 'profile_frame_' + username
        )
        profile_frame.setParent(None)
        profile_frame.deleteLater()

    def open_edit_profile_view(self, profile_info: dict) -> None:
        self._edit_profile_view.setup_view(self._group_index, profile_info)

    def get_profile_info_string(self, profile_username: str) -> str:

        profile = self._groups_controller.get_group_profile_info(
            self._group_index, profile_username
        )

        username = profile.get('username')
        password = profile.get('password')
        gender = profile.get('gender')
        status = profile.get('status')
        current_log = profile.get('current_log')
        like_actions_done = profile.get('like_actions_done')
        follow_actions_done = profile.get('follow_actions_done')
        comment_actions_done = profile.get('comment_actions_done')

        profile_info = f"""        
        Usuário: {username}
        Senha: {password}
        Geênero: {'Masculino' if gender == 'M' else 'Feminino'}
        Status: {status}
        Log: {current_log}
        Ações de like: {like_actions_done}
        Ações de follow: {follow_actions_done}
        Ações de comentário: {comment_actions_done}
        """
        return profile_info
