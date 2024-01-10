import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel  # Gantilah dengan impor yang sesuai dengan model Anda

def save_model_and_tokenizer(model, tokenizer, model_path='your_model.pth', tokenizer_path='your_tokenizer.pth'):
    # Simpan model
    torch.save(model.state_dict(), model_path)

    # Simpan tokenizer
    torch.save(tokenizer, tokenizer_path)

# Contoh penggunaan
model = GPT2LMHeadModel.from_pretrained('gpt2')  # Gantilah dengan model Anda
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')  # Gantilah dengan tokenizer Anda

save_model_and_tokenizer(model, tokenizer)
