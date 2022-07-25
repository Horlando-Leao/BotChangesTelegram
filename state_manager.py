class StateManager:
    def __init__(self, new):
        self.actual = {}
        self.new = new

    @staticmethod
    def __get_id(value: dict) -> str:
        return value.get('id')

    def get_id_actual(self):
        return self.__get_id(self.actual)

    def get_id_new(self):
        return self.__get_id(self.new)

    def is_diff(self) -> bool:
        """
        check bool, if var state_actual != var state_new
        :return:
        """
        check = self.get_id_actual() != self.get_id_new()
        return check

    def set_next_state(self):
        """
        set state actual = new and new = {}
        :return:
        """
        self.actual = self.new
        self.new = {}
