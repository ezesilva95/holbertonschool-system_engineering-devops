#!/usr/bin/env ruby
#Regular expression must match 'hbtn, htn'
puts ARGV[0].scan(/hb?tn/).join()
