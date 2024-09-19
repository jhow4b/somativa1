import unittest
from unittest.mock import patch
import builtins

# Função a ser testada
def jogar():
    print("Selecione uma opção:")
    print("1- Atacar")
    print("2- Bolsa de itens")
    print("3- Fugir")
    escolha = int(input("Qual a sua escolha meu camarada? "))
    match escolha:
        case 1:
            result = "Atacou"
        case 2:
            result = "Abriu sua bolsa de itens"
        case 3:
            result = "Fugiu"
        case _:
            result = "Opção invalida"
    print(result)

class TestJogar(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_opcao_atacar(self, mock_print, mock_input):
        jogar()
        mock_print.assert_any_call("Selecione uma opção:")
        mock_print.assert_any_call("Atacou")
    
    @patch('builtins.input', side_effect=['2'])
    @patch('builtins.print')
    def test_opcao_bolsa_de_itens(self, mock_print, mock_input):
        jogar()
        mock_print.assert_any_call("Selecione uma opção:")
        mock_print.assert_any_call("Abriu sua bolsa de itens")
    
    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_opcao_fugir(self, mock_print, mock_input):
        jogar()
        mock_print.assert_any_call("Selecione uma opção:")
        mock_print.assert_any_call("Fugiu")
    
    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')
    def test_opcao_invalida(self, mock_print, mock_input):
        jogar()
        mock_print.assert_any_call("Selecione uma opção:")
        mock_print.assert_any_call("Opção invalida")
    
    @patch('builtins.input', side_effect=['0'])
    @patch('builtins.print')
    def test_opcao_invalida_baixa(self, mock_print, mock_input):
        jogar()
        mock_print.assert_any_call("Selecione uma opção:")
        mock_print.assert_any_call("Opção invalida")

if __name__ == '__main__':
    unittest.main()

