#!/usr/bin/env ruby
# Matches "hbtn" followed by 2 to 5 occurrences of "t", and ends with "n"
puts ARGV[0].scan(/hbt{2,5}n/).join
