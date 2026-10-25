# Markys SGA Odonto — Gestão de fila odontológica para Windows

Aplicação local para organizar a recepção, a sala de espera e os consultórios de uma clínica odontológica. Esta etapa aproveita o fluxo existente de fila compartilhada, chamadas por voz e acompanhamento de atendimento. **Ainda não substitui um prontuário odontológico completo**: odontograma, anamnese clínica, plano de tratamento, orçamento e financeiro precisam ser implementados e validados antes de uso clínico.

## Estrutura
- `index.html`: recepção e painel público da sala de espera.
- `consultorio.html`: painel da equipe clínica.
- `logo-favmed.png`: logotipo atual (pode ser substituído pelo logotipo da clínica odontológica).
- `servidor-favmed.ps1`: servidor HTTP local para Windows PowerShell 5.1+.
- `fila.json`: dados operacionais locais, criado automaticamente.
- `midia.json` e `midia-sala/`: configuração e arquivos opcionais da tela de espera.
- `documentos-pacientes/`: PDFs anexados, armazenados no computador servidor.
- `INICIAR-SERVIDOR-FAVMED.bat`: inicialização do servidor.
- `INSTRUCOES-REDE-LOCAL.txt`: configuração da rede local.

## Executar
1. Baixe o ZIP da branch `adaptacao-odontologia` e extraia para uma pasta permanente no computador servidor.
2. Execute `INICIAR-SERVIDOR-FAVMED.bat`.
3. Use os endereços e a porta mostrados pela janela do servidor. A configuração atual tenta a porta TCP `2222`; se estiver ocupada, o servidor encerra com aviso.
4. Para acessar de outros dispositivos, use o endereço IPv4 do computador servidor e a mesma porta, na mesma rede local.

## Escopo atual herdado
O projeto original oferece cadastro operacional, fila por sala/serviço, chamadas, status por atendimento, atualização entre telas, exportação e backup. Esses recursos precisam passar por testes de regressão após a adaptação odontológica.

## Antes de usar com pacientes reais
- A versão atual não oferece autenticação nem criptografia; não a exponha à internet nem a redes Wi-Fi públicas.
- Dados de saúde são sensíveis. Restrinja o acesso ao computador e à pasta de dados, mantenha backups protegidos e não coloque dados reais em commits ou no GitHub.
- Não use a fila como substituto do prontuário clínico oficial. Registre procedimentos, evolução e documentos em sistema adequado até que os módulos odontológicos sejam desenvolvidos e validados.
- Não considere este software, por si só, como garantia de conformidade com a LGPD ou com normas profissionais.

## Próximas etapas recomendadas
1. Corrigir e testar o servidor e as rotas de recepção/consultório.
2. Adaptar os cadastros para agenda, dentista, cadeira e tipo de consulta.
3. Criar prontuário odontológico com anamnese, odontograma por dente/face, evolução e anexos.
4. Ligar plano de tratamento e orçamento ao financeiro.
5. Implementar autenticação, perfis de acesso, trilha de auditoria e backup protegido.
6. Testar com dados fictícios antes de qualquer uso real.

