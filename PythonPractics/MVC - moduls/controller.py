import text
import view
import model
def start_app():
    while True:
        print(text.main_menu)
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_massage(text.load_successful)
            case 2:
                pass
            case 3:
                pb = model.phone_book
                view.show_contacts()
            case 4:
                contact = view.add_contact(text.new_contact)
                model.new_contact(contact)
                view.print_massage(text.new_contact_added_successfully)
            case 5:
                word = view.imput_data(text.imput_search_word)
                result = model.find_contact(word)
                view.show_contacts(result)
            case 6:
                model.find_contact()
                view.imput_data(text.input_id_change_contact)
                model.change_contact()
            case 7:
                break