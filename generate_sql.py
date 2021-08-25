import random
from faker import Faker

fakegen = Faker()

school_num = 2
user_num = 50
school_user_num = user_num / school_num
teacher_num = 5
report_card_num = user_num
subject_num = 4


def generate_user():
    sql = 'INSERT INTO %s VALUES (\'%s\', \'%s\', hex(AES_ENCRYPT(\'%s\', @key_str)), \'%s\', \'%s\');'
    table_name = 'USER'

    for i in range(0, user_num):
        if i < school_user_num:
            offset = 0
            school_id = 'S000'
        if i >= school_user_num and i < school_user_num * 2:
            offset = school_user_num
            school_id = 'S001'

        user_id = 'U{:03}'.format(i)
        user_name = fakegen.name()
        email = fakegen.email()
        if i < offset + teacher_num:
            teacher_id = ''
        else:
            teacher_id = 'U{:03}'.format(random.randint(offset + 0, offset + teacher_num - 1))

        print(sql % (table_name, user_id, user_name, email, school_id, teacher_id))


def generate_report_card():
    sql = 'INSERT INTO %s VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');'
    table_name = 'REPORT_CARD'

    for i in range(0, user_num):
        if i < school_user_num:
            offset = 0
        if i >= school_user_num and i < school_user_num * 2:
            offset = school_user_num

        report_card_id = 'R{:03}'.format(i)
        user_id = 'U{:03}'.format(i)
        first_evaluator_id = 'U{:03}'.format(random.randint(0 + offset, teacher_num + offset - 1))
        second_evaluator_id = 'U{:03}'.format(random.randint(0 + offset, teacher_num + offset - 1))
        content = fakegen.text(50)

        print(sql % (table_name, report_card_id, user_id, first_evaluator_id, second_evaluator_id, content))


def generate_subject():
    sql = 'INSERT INTO %s VALUES (\'%s\', \'%s\', \'%s\');'
    table_name = 'SUBJECT'

    for i in range(0, report_card_num):
        if i < school_user_num:
            offset = 0
        if i >= school_user_num and i < school_user_num * 2:
            offset = school_user_num

        report_card_id = 'R{:03}'.format(i)

        for j in range(0, subject_num):
            if j == 0:
                offset = 0
                content = 'English'
            if j == 1:
                offset = report_card_num
                content = 'Math'
            if j == 2:
                offset = report_card_num * 2
                content = 'Science'
            if j == 3:
                offset = report_card_num * 3
                content = 'Social'
            _j = i + offset
            subject_id = 'S{:03}'.format(_j)

            print(sql % (table_name, subject_id, report_card_id, content))


if __name__ == '__main__':
    generate_user()
