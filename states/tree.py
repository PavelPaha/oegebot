from aiogram.dispatcher.filters.state import StatesGroup, State


class les_tree(StatesGroup):
    main = State()

    ege_menu = State()
    ege_select_lesson = State()
    ege_select_option = State()

    ege_random_task = State()
    ege_numbers = State()
    ege_reference_information = State()
    ege_clock = State()

    ege_end = State()

    # ГЕОГРАФИЯ
    ege_geogr = State()

    ege_geogr_practice = State()
    ege_geogr_num = State()
    ege_geogr_refinf = State()
    ege_geogr_clock = State()


    ege_liter = State()
    ege_obshestv = State()
    ege_history =  State()
    ege_rus = State()
    ege_math_base = State()

    # МАТЕМАТИКА ПРОФИЛЬ
    ege_math_prof = State()
    ege_math_practice = State()

    ege_math_num = State()
    ege_math_num_edit = State()

    ege_math_refinf = State()
    ege_math_clock = State()


    ege_phys = State()
    ege_bio = State()
    ege_chim = State()
    ege_inf = State()
    ege_en = State()
    ege_deu = State()
