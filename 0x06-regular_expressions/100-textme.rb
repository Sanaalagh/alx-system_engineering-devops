#!/usr/bin/env ruby
# Matches specific patterns for sender, receiver, and flags
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
