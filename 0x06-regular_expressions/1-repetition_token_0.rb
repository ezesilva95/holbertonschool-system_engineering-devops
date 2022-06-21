#!/usr/bin/env ruby
#Regular expression must match 'hbttn, hbtttn, hbttttn, hbtttttn' cases
puts ARGV[0].scan(/hbt{2,5}n/).join()
