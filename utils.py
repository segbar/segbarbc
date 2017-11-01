from config import *
import datetime
import block

def is_valid_chain():
  '''
    We need to check to see if the entire chain is valid.
    To do this, we check if each block in order is valid.
    The is_valid() function in the Block class handles the
    hash connection between the previous and current block.
  '''
  for b in blockchain:
    if not b.is_valid():
      return False
  return True

def dict_from_block_attributes(**kwargs):
  info = {}
  for key in kwargs:
    if key in BLOCK_VAR_CONVERSIONS:
      info[key] = BLOCK_VAR_CONVERSIONS[key](kwargs[key])
    else:
      info[key] = kwargs[key]
  return info

def create_new_block_from_prev(prev_block=None):
  if not prev_block:
    # index zero and arbitrary previous hash
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = ''
    block_data['nonce'] = 0 #starting it at 0
    return block.Block(block_data)
  else:
    index = int(prev_block.index) + 1
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    data = "I block #%s." % (int(prev_block.index) + 1) #random string for now, not transactions
    prev_hash = prev_block.hash
    nonce = 0
    block_info_dict = dict_from_block_attributes(index=index, timestamp=timestamp, data=data, prev_hash=prev_hash, nonce=nonce)
    new_block = block.Block(block_info_dict)
    return new_block
