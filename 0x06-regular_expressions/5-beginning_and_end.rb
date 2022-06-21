#!/usr/bin/env ruby
#Regular expression that must match a string  that starts with h ends with n
#With any single charater in between
puts ARGV[0].scan(/h.n/).join()
