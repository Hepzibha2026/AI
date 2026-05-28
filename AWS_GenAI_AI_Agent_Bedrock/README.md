Getting started with AWS Generative AI for Developers
- Foundation models
- low level APIs
- integrate AI feautures into our applications
- asynchronous and batch inference
- writing prompts in Natural language
- bedrock guardrails

course roadmap
Pre-AI Era
- Rules based systems with strict algorithms
Rise of Machine Learning
- Models trained on data for pattern recognition
Emergence of Deep Learning
- Neural networks with many layers
Human-like performance
- AI achieving human-level performance.
- GPUs
- deep learning to handle complex patterns in data

Generative AI is the sub set of deep learning
Deep learning
- This broader field of AI that Generative AI belongs to 
- LLM-Large language models
   - The core technology behind Generative AI
 - Training Materials
    - Training data comes from a wide variety of materials
  - Pattern Recognition
    - The ability of LLMs to identify structures in text

-context
-parameters

Initial Random Parameters 
- The model starts with random parameter settings.
Training 
- The model learns from a large datasets
Parameter Fine-Tuning
- Parameters are adjusted to improve predictions.
Model Trained
- The model is ready for various tasks.
Use model in Applications

Multi-modal models - LLM -> beyond processing text
Foundation models -
 pre-trained -> Foundation models -> wide range of tasks
                    |
                    v
                Fine-tune for specific tasks

foundation models - it can process and generate different types of data- broader category of deep learning models

Amazon Bedrock - serverless access to pre-trained foundation models through API calls
Bedrock host the models and invoke it through a hosted API

send prompt -> model performs inference -> receive response
send prompt - the user sends a prompt to the model using the hosted APIs
model performs inference - The model processes the prompt to generate an output
receive response - The user received the model's response
inference - inference is the term used for the processes of running data through a trained model to generate an output.
tools - 
Amazon Bedrock - use the foundation model through Amazon Bedrock fine-tune it with our own data if needed and invoke it easily using the API with our application code.
-summarization tools, code generation, and eveb creative applications like AI powered design and writing assistance

how to integrate bedrock in my application
What capability allows a trained language model to condense long passages?
- summarizing text
Create using the generative AI features of Amazon Bedrock
use case directly in the console -
AWS service - 
Bedrock is available via an API and SDKs for lot of programming languages.
how we can use Bedrock for generative AI from code.
Bedrock console
- under "playground" in left side pannel
- choose "chat/text"
- button "select model"
- we can see a list of many different model providers
- choose the Amazon Nova Pro model
- This Amazon Nova Pro model work with both text and vision
- In this model selection left side pannel
- we can see the parameters like "Temperature" and "Top p"
- These above parameters control the randomness and diversity of the response.
- At the bottom, We have a text input for a prompt
- The prompt is input to send to the model for a response.
- This can be a natural language instruction to describe what we want generated and the output is text.
- if run several time - give several different output - this output is non-deterministic.  That actually a property of the temperature setting over here.
- Then i choose the image/ video playground
- select the model
- select "Nova Canvas"
- give the prompt and get the image output 

Terms to remember
Model - foundation model
different providers and models for different inputs and outputs 
prompt - input to the model is called prompt
prompt is the input instruction used by the model to generate the output
Prompt Engineering - The process of writing and improving prompts is called prompt engineering

What we have to do to generate text and images from an application?
use the Bedrock API
boto3 - boto3 is the AWS SDK for python
This is how we can call AWS APIs from my python code.

low level API invoke model

Generative AI Applications with Amazon Bedrock

Amazon Bedrock customization, optimization & automation

Amazon Q Developer

OWASP - Open Worldwide Application Security Project
Dev Agent - assists in writing, refactoring, and optimizing code
Test agent -
Review agent -
Transform agent - 
Doc agent - 
conversational interface

Vibe coding - vibe coding is taking the internet by storm and essentially what this is working with and AI assistant to create full applications and letting the AI do most of the coding.
tool set - 
T - trust in Q developer
3D Whack a mole game

Doc2FAQ - allow uploads of documents

MVN clean
MVN install

invoke model
inference performance tuning
bedrock runtime APIs
stream responses
synchronous call

low-level API
payload structure
amazon tital text model
text generation config.

MU - model unit

start-async-invoke or
create-model-invocation-job APIs

Amazon nova reel model

bedrock - control plane
bedrock-runtime - data plane
bedrock agent - control plane
bedrock-agent runtime - data plane

Guardrails - Guardrails offer several different categories - prompt attacks, denied topics, personally identifiable information,  grounding and relevance.

Model categories and capabilities:
- Text generation models
- Conversational models
- image processing models
- video generation models
- multimodal models.
  
Technical requirements
- input / output capabilities
  - supported content types - text, image, video
  - Token limits
  - Response time requirements
  - API structure compatibility
- Performance metrics:
  - Latency expectations
  - Accuracy requirements
  - Processing capability
  - Memory usage
  
Business considerations
- Cost structure
  - input / output token pricing
  - API call charges
  - Expected volume costs
  - Total cost of ownership
- Compliance and scale
  - Data privacy requirements
  - industry regulations
  - Growth projections
  - Geographic needs.

Prompt caching
converse API




Amazon Bedrock :
    Amazon Bedrock is a fully managed service that makes foundation models leading AI companies accessible through a unified API.  Whether you're building conversational AI applications, content generation tools, or automated analysis systems, Amazon Bedrock provides the infrastructure and models you need to bring generative AI compatibilities into your applications.
