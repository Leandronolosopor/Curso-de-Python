
#del github de la profe
from typing import Union

def process_salary(salary: Union[int, float]) -> float:#union nos da la posibilidad de poner
    #mas de un tipo de dato, mientras que option solo nos deja un tipo de dato y si no es ese
    #entonces es un non, en cambio union puedo poner int, float, str y eso
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)