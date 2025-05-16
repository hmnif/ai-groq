from groq import Groq

# Inisialisasi klien Groq
client = Groq(api_key="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")

# Inisialisasi riwayat percakapan
chat_history = []

def chat_with_groq():
    response = client.chat.completions.create(
        # model="llama3-8b-8192",
        model="deepseek-r1-distill-llama-70b",
        messages=chat_history  # Kirim seluruh riwayat
    )
    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    return reply

if __name__ == "__main__":
    print("Welcome to the AI Chatbot! 🤖")
    # print("Ketik 'quit' untuk keluar.\n")
    while True:
        # print("Welcome to the AI Chatbot! 🤖")
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye! Nice to meet you. 👋")
            break

        # Tambahkan pesan pengguna ke riwayat
        chat_history.append({"role": "user", "content": user_input})

        # Dapatkan respons dari Groq dan tampilkan
        response = chat_with_groq()
        print("Chatbot:", response)
        print("\nKetik 'quit' untuk keluar.")
