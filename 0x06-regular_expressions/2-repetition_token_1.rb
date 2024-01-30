#!/usr/bin/env ruby
# Matches "hbtn" followed by 0 or more occurrences of "t", and ends with "n"
puts ARGV[0].scan(/hbt*n/).join
