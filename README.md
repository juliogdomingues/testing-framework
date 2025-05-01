# testing-framework

Este repositório contém um MVP de um framework de teste inspirado no padrão xUnit, desenvolvido como atividade prática da disciplina Teste de Software (DCC/UFMG), do professor André Hora.

Aluno: Júlio Guerra Domingues

Matrícula: 2022431280

## Estrutura dos Arquivos

- **framework.py**  
  Implementação do framework de teste, incluindo:
  - `TestCase`: Classe base para casos de teste, com métodos de asserção (`assert_equal`, `assert_true`, etc.).
  - `TestResult`: Coleta e sumariza os resultados dos testes.
  - `TestSuite`: Permite agrupar e executar múltiplos testes.
  - `TestLoader`: Descobre métodos de teste automaticamente e monta suítes.
  - `TestRunner`: Executa as suítes de teste e exibe o relatório.

- **tests.py**  
  Testes automatizados para validar o funcionamento do framework, incluindo:
  - `TestStub` e `TestSpy`: Classes auxiliares para testar o framework.
  - `TestCaseTest`, `TestSuiteTest`, `TestLoaderTest`: Testam as funcionalidades das respectivas classes do framework.
  - O bloco principal executa todos os testes usando o próprio framework.

- **instructions.md**  
  Documento com as instruções detalhadas para implementação do framework, baseado no livro "Test Driven Development: By Example" de Kent Beck.

## Como Executar os Testes

1. Certifique-se de estar na raiz do repositório.
2. Execute o arquivo de testes com Python 3:

   ```sh
   python3 tests.py
   ```
3. O resultado exibirá um resumo da execução dos testes, por exemplo:
   ```
   19 run, 0 failed, 0 error
   ```

## Observações

- Não é necessário instalar dependências externas, pois todo o framework foi implementado do zero.
- Os testes são executados utilizando o próprio framework desenvolvido neste projeto.

---

_Este README foi construído com o auxílio de LLM (GitHub Copilot, GPT-4.1, maio/2025)._




