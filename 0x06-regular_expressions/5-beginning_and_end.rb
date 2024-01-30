#!/usr/bin/env ruby
# Matches "h", any single character, and "n"
puts ARGV[0].scan(/h.n/).join
