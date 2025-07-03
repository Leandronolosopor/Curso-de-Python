#Este archivo lo pego del github de la profe
from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:#Optional nos permite
    #que el tipo de dato no sea solo el que definimos, sino que si no se devuelve el anotado
    #sea entonces un none
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None