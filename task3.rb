SOUND_SPEED_mS = 340.0 / 1000

measurement = readlines.join(' ').split(' ').map { |value| value.to_f }
count = measurement.shift.to_i

intervals = []
measurement.each_slice(2) do |pair|
  intervals.push pair[1]-pair[0]
end

intervals.sort!
intervals.insert count/2, intervals[count/2] if count.odd?

median_interval = intervals.slice(intervals.count/2-1,2).reduce(&:+)

puts (median_interval / 4.0) * SOUND_SPEED_mS
