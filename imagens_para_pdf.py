
from PIL import Image
import os
import glob

pasta = "img"
extensoes = ["*.jpg", "*.jpeg", "*.png", "*.webp"]
arquivos = []

for extensao in extensoes:
    arquivos.extend(glob.glob(os.path.join(pasta, extensao)))

# Ordena os arquivos pelo nome
arquivos.sort()

# converte as imagens
imagens = []

for arquivo in arquivos:
    imagem = Image.open(arquivo)
    imagem = imagem.convert("RGB")
    imagens.append(imagem)

# Gera o PDF
if imagens:
    imagens[0].save(
        "resultado.pdf",
        save_all=True,
        append_images=imagens[1:]
    )
    print(f"PDF criado com {len(imagens)} imagens!")
else:
    print("Nenhuma imagem encontrada na pasta img.")
