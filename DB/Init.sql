CREATE TABLE instituicoes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100),
  tipo VARCHAR(50),
  cidade VARCHAR(50),
  necessidade VARCHAR(150)
);

INSERT INTO instituicoes (nome, tipo, cidade, necessidade) VALUES
  ('Escola Municipal João XXIII', 'Escola Pública', 'Crato', 'Cadernos, lápis e mochilas para alunos do fundamental'),
  ('ONG Ler é Viver', 'ONG', 'Fortaleza', 'Livros didáticos e paradidáticos do ensino médio'),
  ('Projeto Horta Escola', 'Projeto Social', 'Juazeiro do Norte', 'Sementes, ferramentas e materiais recicláveis');