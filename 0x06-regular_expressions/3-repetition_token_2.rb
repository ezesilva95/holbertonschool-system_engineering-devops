#!/usr/bin/env ruby
#Regular expresion taht must match 'hbtn, hbttn, hbtttn, hbttttn'
puts ARGV[0].scan(/hbt+n/).join()
