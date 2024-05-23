import UrbanRoutesPage
import helpers
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()

class TestUrbanRoutes:

    driver = webdriver.Chrome

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--windows-size=1920x1080")
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_directions_are_ok(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        directions_from = data.address_from
        directions_to = data.address_to
        assert routes_page.get_from() == directions_from
        assert routes_page.get_to() == directions_to

    def test_ask_for_a_taxi(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.set_from()
        routes_page.set_to()
        helpers.wait_for_ask_taxi_button()
        routes_page.click_ask_for_taxi_button()
        helpers.wait_for_reserve_button()
        assert True, expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'np-button'))

    def test_select_comfort_category(self):
        # Prueba para validar que la tarifa "Comfort" a sido seleccionada.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_comfort_category()
        assert True, expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[1]'))

    def test_set_phone_number(self):
        # Prueba para introducir un número telefónico.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        # Obtener el Código SMS para validación.
        routes_page.fill_phone_number()
        helpers.standard_wait_time()
        assert routes_page.text_in_phone_number_box == phone_number

    def test_add_card_code(self):
        # Prueba para agregar una tarjeta de pago.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        # proceso del metodo de pago
        routes_page.set_steps_payment_method(card_number, card_code)
        # verificación que el metodo de pago funcionó
        assert True, routes_page.check_agree_card()
        # cierre de ventana de metodo de pago
        routes_page.click_close_pop_up_card_windows()

    def test_message_for_driver(self):
        # Prueba para agregar un mensaje al conductor.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Ingresar el mensaje del conductor
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_blanket_is_selected(self):
        # Prueba para agregar una manta y pañuelos.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hacer click en el slider
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'

    def test_add_2_ice_creams(self):
        # Prueba agregar 2 helados a la ruta.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'

    def test_taxi_request_modal_display(self):
        # Prueba para esperar que aparezca la información del conductor en el modal.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        assert True, routes_page.check_header_order_title()

    def test_check_show_name_driver_modal(self):
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        helpers.wait_for_countdown_to_finish()
        assert True, routes_page.check_taxi_driver_is_selected()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
