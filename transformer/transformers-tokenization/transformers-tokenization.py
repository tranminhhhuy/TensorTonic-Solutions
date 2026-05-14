import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """

        self.word_to_id[self.pad_token]=0
        self.word_to_id[self.unk_token]=1
        self.word_to_id[self.bos_token]=2
        self.word_to_id[self.eos_token]=3

        self.id_to_word[0]=self.pad_token
        self.id_to_word[1]=self.unk_token
        self.id_to_word[2]=self.bos_token
        self.id_to_word[3]=self.eos_token

        sorted_word=set()
        idx= 4
        for text in texts:
            word=text.lower().split()
            sorted_word.update(word)
        sorted_word=sorted(sorted_word)
        for words in sorted_word:
            if words not in self.word_to_id:
                self.word_to_id[words]=idx
                self.id_to_word[idx]=words
                idx+=1
        
        self.vocab_size = len(self.word_to_id)
        
        # YOUR CODE HERE
        pass
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        texts=text.lower().split()
        token_id=[]
        for word in texts :
            if word not in self.word_to_id:
                token_id.append(self.word_to_id[self.unk_token])
            else:
                token_id.append(self.word_to_id[word])
                
        return token_id
        # YOUR CODE HERE
        pass
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words= []
        for id in ids:
            if id not in self.id_to_word:
                words.append(self.unk_token)
            else: 
                words.append(self.id_to_word[id])
        return " ".join(words)
        pass
