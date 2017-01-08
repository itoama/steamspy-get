require 'steamspy'
require 'csv'

steamspy = SteamSpy::Api.new

#ss = steamspy.appdetails(730)
#puts ss.status
#puts ss.data

ss = steamspy.genre("Early Access")

hash = ss.data
puts hash
p hash.keys
h = hash.keys
p h.length


#データの保存
#CSV.open("data.csv", "a+") do |csv|
#  csv << hash.keys
#  csv << hash.values
#end



#open(j.json, 'w') do |io|
#  JSON.dump(hash, io)
#end



#ss.class
