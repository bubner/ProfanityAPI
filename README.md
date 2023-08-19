# ProfanityAPI
### Live at https://profanityapi.vercel.app/f?=TEXT
WSGI API runner for [profanity-check](https://github.com/vzhou842/profanity-check). <br>
View their documentation for more information on their SVM model. <br>
Using the [alt-profanity-check](https://github.com/dimitrismistriotis/alt-profanity-check) fork to support later versions of scikit-learn. Many thanks!
# Example usage
Input:  
```/?f=fuck```  <br> <br>
Output:
```
{
  "probability": 0.9999999997233655,
  "profane": true,
  "text": "fuck"
}
```
___
Input:
```/?f=hello```  <br> <br>
Output:
```
{
  "probability": 0.03218035443843418,
  "profane": false,
  "text": "hello"
}
```
___
Input:
```/?f=you are strange```  <br> <br>
Output:
```
{
  "probability": 0.06342308936201688,
  "profane": false,
  "text": "you are strange"
}
```
___
Input:
```/?f=do%20us%20a%20favour%20and%20remove%20yourself%20from%20the%20face%20of%20the%20planet```  <br> <br>
Output:
```
{
  "probability": 0.23342035478746662,
  "profane": false,
  "text": "do us a favour and remove yourself from the face of the planet"
}
```
___
Input:
```/?f=go%20away%20you%20bum```  <br> <br>
Output:
```
{
  "probability": 0.4761022259622523,
  "profane": false,
  "text": "go away you bum"
}
```