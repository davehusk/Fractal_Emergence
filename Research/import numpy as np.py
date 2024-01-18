from typing import List, Tuple
import logging
import math
import openai
import numpy as np
from typing import List, Tuple
import math
import logging
import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
import openai
import numpy as np

app = FastAPI()
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

class IntentData(BaseModel):
    intent: str
    prob: float

class ResponseData(BaseModel):
    response: str
    prob: float

def calc_entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def calc_conditional_entropy(joint_probs, marginal_probs):
    conditional_entropies = []
    for i in range(len(joint_probs)):
        conditional_entropy = 0
        for j in range(len(joint_probs[i])):
            if joint_probs[i][j] > 0 and marginal_probs[i] > 0:
                conditional_entropy -= joint_probs[i][j] * (math.log2(joint_probs[i][j]) - math.log2(marginal_probs[i]))
        conditional_entropies.append(conditional_entropy)
    return conditional_entropies

def calc_mutual_information(entropy_X, entropy_Y, conditional_entropy_XY):
    MI = entropy_X + entropy_Y - conditional_entropy_XY
    return MI

@app.post("/generate_response")
async def generate_response(user_intent: IntentData) -> ResponseData:
    user_intents = ["greetings", "question"]
    user_intent_probabilities = [0.6, 0.4]

    response_options = ["Great! How can I assist you?", "Please feel free to ask any questions."]
    marginal_response_pr = np.ones(len(response_options)) / len(response_options)

    response_from_open_ai = ""  # Replace with the real call to the OpenAi GPT Model

    initial_state_mutual_info = calc_mutual_information(
        calc_entropy(user_intent_probabilities),
        calc_entropy(marginal_response_pr),
        calc_conditional_entropy(np.outer(np.array(user_intent_probabilities), np.array(marginal_response_pr)), marginal_response_pr),
    )

    logging.info("Initial state mutual information: %.8f", initial_state_mutual_info)

    logging.info("Open AI generated response:", response_from_open_ai)

    final_response_options = ["{} {}".format(response_from_open_ai, opt) for opt in response_options]

    joint_r_ps = []
    for option in final_response_options:
        final_response_ps = await get_response_probability(option)  # Assuming there's a function 'get_response_probability' to obtain the probability of a specific response
        joint_r_ps.append((float(option.split(' ')[0].strip()) == user_intent.intent, final_response_ps))

    final_state_mutual_info = calc_mutual_information(
        calc_entropy([p[0] for p in joint_r_ps]),
        calc_entropy(np.array([p[1] for p in joint_r_ps])),
        calc_conditional_entropy(np.outer(np.array(user_intent_probabilities), np.array(np.array([p[1] for p in joint_r_ps]).flatten())), np.array([p[1] for p in joint_r_ps])),
    )

    logging.info("Final state mutual information: %.8f", final_state_mutual_info)

    best_match_index = np.argmax([p[0] for p in joint_r_ps])
    selected_response = final_response_options[best_match_index]

    return {"response": selected_response, "prob": max([p[1] for p in joint_r_ps])}
```

class IntentData(BaseModel):
      intent: str
      prob: float

class ResponseData(BaseModel):
      response: str
      prob: float

def calc_entropy(probabilities):
      entropy = 0
      for p in probabilities:
            if p > 0:
                  entropy -= p * math.log2(p)
      return entropy

def calc_conditional_entropy(joint_probs, marginal_probs):
      conditional_entropies = []
      for i in range(len(joint_probs)):
            conditional_entropy = 0
            for j in range(len(joint_probs[i])):
                  if joint_probs[i][j] > 0 and marginal_probs[i] > 0:
                        conditional_entropy -= joint_probs[i][j] * (math.log2(joint_probs[i][j]) - math.log2(marginal_probs[i]))
            conditional_entropies.append(conditional_entropy)
      return conditional_entropies

def calc_mutual_information(entropy_X, entropy_Y, conditional_entropy_XY):
      MI = entropy_X + entropy_Y - conditional_entropy_XY
      return MI

@app.post("/generate_response")
async def generate_response(user_intent: IntentData) -> ResponseData:
      user_intents = ["greetings", "question"]
      user_intent_probabilities = [0.6, 0.4]

      response_options = ["Great! How can I assist you?", "Please feel free to ask any questions."]
      marginal_response_pr = np.ones(len(response_options)) / len(response_options)

      response_from_open_ai = ""  # Replace with the real call to the OpenAi GPT Model

      initial_state_mutual_info = calc_mutual_information(
            calc_entropy(user_intent_probabilities),
            calc_entropy(marginal_response_pr),
            calc_conditional_entropy(np.outer(np.array(user_intent_probabilities), np.array(marginal_response_pr)), marginal_response_pr),
      )

      logging.info("Initial state mutual information: %.8f", initial_state_mutual_info)

      logging.info("Open AI generated response:", response_from_open_ai)

      final_response_options = ["{} {}".format(response_from_open_ai, opt) for opt in response_options]

      joint_r_ps = []
      for option in final_response_options:
            final_response_ps = await get_response_probability(option)  # Assuming there's a function 'get_response_probability' to obtain the probability of a specific response
            joint_r_ps.append((float(option.split(' ')[0].strip()) == user_intent.intent, final_response_ps))

      final_state_mutual_info = calc_mutual_information(
            calc_entropy([p[0] for p in joint_r_ps]),
            calc_entropy(np.array([p[1] for p in joint_r_ps])),
            calc_conditional_entropy(np.outer(np.array(user_intent_probabilities), np.array(np.array([p[1] for p in joint_r_ps]).flatten())), np.array([p[1] for p in joint_r_ps])),
      )

      logging.info("Final state mutual information: %.8f", final_state_mutual_info)

      best_match_index = np.argmax([p[0] for p in joint_r_ps])
      selected_response = final_response_options[best_match_index]

      return {"response": selected_response, "prob": max([p[1] for p in joint_r_ps])}
