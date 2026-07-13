import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {} # self.word to id [str -> int] example : {"hello": 4, "world": 5}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None: # stag2 
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        # add special tokens
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        for token in special_tokens:   
            self.word_to_id[token]=self.vocab_size
            self.id_to_word[self.vocab_size]=token
            self.vocab_size+=1

        # add unique words 
        unique_words = set()
        for text in texts:
            words= text.split()
            unique_words.update(words)
        unique_words=sorted(unique_words)# sorted to ensure consistent ordering

        for word in unique_words:
            self.word_to_id[word]=self.vocab_size
            self.id_to_word[self.vocab_size]=word
            self.vocab_size+=1



        pass
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """

        # YOUR CODE HERE
        text=text.lower()
        tokens=text.split()
        token_ids=[]
        for token in tokens:
            if token in  self.word_to_id:
                token_ids.append(self.word_to_id[token])
            else:
                token_ids.append(self.word_to_id[self.unk_token])
        return token_ids
        pass
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words=[]
        for id in ids:
            if id in self.id_to_word:
                words.append(self.id_to_word[id])
            else:
                words.append(self.unk_token)
        return ' '.join(words)
    pass