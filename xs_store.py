
class xs_store(object):
    def store(self, data):
        try :
            with open("zhenghun.csv", 'a+') as f:
                for d in data:
                    #f.write(d[0]+"  "+d[1])
                    #d1 = str(d[0]).encode('utf-8')
                    #d2 = str(d[1]).encode('gbk')
                    #print(type(d[0]))
                    #print(type(d[1]))
                    f.write(d[0])
                    f.write(" ")
                    f.write(d[1])
                    f.write("\n")
        except:
            print("store error")


