#!/usr/bin/env ruby
puts ARGV[0].scan(/from:.\w*/).join.slice(5..-1)
puts ARGV[0].scan(/to:.\w*/).join.slice(3..-1)
puts ARGV[0].scan(/flags:(-?\d:?)(-?\d:?)(-?\d:?)(-?\d:?)(-?\d:?)/).join
