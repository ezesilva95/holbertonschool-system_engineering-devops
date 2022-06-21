#!/usr/bin/env ruby
#Regular expression must match 'hbn, hbtn, hbttn, hbtttn, hbtttttn'
puts ARGV[0].scan(/hbt*n/).join()
