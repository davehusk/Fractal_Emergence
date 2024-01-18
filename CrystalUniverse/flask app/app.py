from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "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"
openai.api_base = "https://api.perplexity.ai/"
openai.engine = "mixtral-8x7b-instruct"

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
      user_input = request.form['user_input']
      try:
            response = openai.Completion.create(
                  model=openai.engine,
                  prompt=user_input,
                  max_tokens=100
            )
            code = response.choices[0].text.strip()

            print(code)

            return render_template('index.html', generated_code=code)
      except Exception as e:
            return render_template('index.html', generated_code='', error=str(e))

  return render_template('index.html', generated_code='')

if __name__ == '__main__':
    app.run(debug=True)