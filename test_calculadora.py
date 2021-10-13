import calculadora


def test_suma():

    # Arrange
    numero_de_prueba = 4

    # Act
    numero_obtenido = calculadora.suma(2, 2)

    # Assert
    assert numero_obtenido == numero_de_prueba
 

def test_resta():

    # Arrange
    numero_de_prueba = 0

    # Act
    numero_obtenido = calculadora.resta(2, 2)

    # Assert
    assert numero_de_prueba == numero_obtenido


def test_multiplicacion():

    # Arrange
    numero_de_prueba = 4

    # Act
    numero_obtenido = calculadora.multiplicacion(2, 2)
 
    # Assert
    assert numero_de_prueba == numero_obtenido


def test_division():

    # Arrange
    numero_de_prueba = 1

    # Act
    numero_obtenido = calculadora.division(2, 2)

    # Assert
    assert numero_de_prueba == numero_obtenido

    
def test_potencia():
    
    # Arrange
    numero de prueba = 8
        
    #act
    numero_obtenido = calculadora.potenciacion(2, 3)
        
    # Assert
    assert numero_de_prueba == numero_obtenido
   
