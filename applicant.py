class Applicant:
    def __init__(
            self,
            full_name,
            vacancy,
            raw_status=None,
            money=None,
            comment=None,
            file_name=None,
            file=None,
    ):
        self.full_name = full_name
        self.vacancy = vacancy
        self.money = money
        self.comment = comment
        self.raw_status = raw_status
        self.file = file
        self.file_name = file_name

        self.first_name = ''
        self.last_name = ''
        self.middle_name = None
        self.phone = None
        self.email = None
        self.position = None
        self.company = None
        self.birthday_day = None
        self.birthday_month = None
        self.birthday_year = None
        self.photo = None
        self.externals = None

    def __str__(self):
        return self.full_name

    def set_name(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            name = fields.get('name')
            if name:
                self.first_name = name.get('first')
                self.last_name = name.get('last')
                self.middle_name = name.get('middle')

        if not self.first_name or not self.last_name:
            separated_name = self.full_name.split(' ')
            self.last_name = separated_name[0]
            self.first_name = separated_name[1]

    def set_phone(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            phones = fields.get('phones')
            if phones:
                self.phone = phones[0]

    def set_email(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            self.email = fields.get('email')

    def set_position(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            experience = fields.get('experience')
            if experience:
                self.position = experience[0].get('position')

    def set_company(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            experience = fields.get('experience')
            if experience:
                self.company = experience[0].get('company')

    def set_birthday(self, parsed_data):
        fields = parsed_data.get('fields')
        if fields:
            birthdate = fields.get('birthdate')
            if birthdate:
                self.birthday_day = birthdate.get('day')
                self.birthday_month = birthdate.get('month')
                self.birthday_year = birthdate.get('year')

    def set_photo(self, parsed_data):
        photo = parsed_data.get('photo')
        if photo:
            self.photo = photo.get('id')

    def set_externals(self, parsed_data):
        body = parsed_data.get('text')
        file_id = parsed_data.get('id')
        if body and file_id:
            text = {'body': body}
            files = [{'id': file_id}]
            self.externals = [{
                'data': text,
                'auth_type': 'NATIVE',
                'files': files,
            }]

    def get_set_methods(self):
        return [method for method in dir(self) if method.startswith('set_')]

    def get_attributes(self):
        exclude_list = ('__', 'get', 'set', 'file')
        return [attr for attr in dir(self) if not attr.startswith(exclude_list)]

    def get_data(self, parsed_data):
        methods = self.get_set_methods()
        for method in methods:
            method = getattr(self, f'{method}')
            method(parsed_data)
        attrs = self.get_attributes()
        return {
            attr: getattr(self, f'{attr}')
            for attr in attrs
        }
