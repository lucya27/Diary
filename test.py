from datetime import datetime

today = datetime.now()

date_time= today.strftime('%Y-%m-%d-%H-%M-%S')

print(date_time)
connection_string = 'mongodb+srv://lucyarayikirana:lucya@cluster0.owq7clu.mongodb.net/?retryWrites=true&w=majority'