from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


def wait_for_ask_taxi_button(self):
    WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.UrbanRoutesPage.ask_for_taxi_button))

def wait_for_reserve_button(self):
    # Esperar que todos los elementos cargen y el botón de reserva sea clickeable.
    WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.UrbanRoutesPage.reserve_button))

def standard_wait_time(self):
    # Esperar a que los elementos cargen por 2 segundos.
    WebDriverWait(self.driver, 2)

def wait_for_countdown_to_finish(self):
    # Esperar a que el timer el pedido llegue a "0".
    WebDriverWait(self.driver, 35).until(expected_conditions.visibility_of_element_located(self.UrbanRoutesPage.taxi_driver_is_selected))
