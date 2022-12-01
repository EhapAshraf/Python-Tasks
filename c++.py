f2=open("file5.cpp","w+")
f2.write("#include<iostream>\nint main(){\nstd::cout<<\"")
message=input("please enter the message : ")
f2.write(message)
f2.write("\"<<std::endl;\n}")

f2.close()
subprocess.call(["g++", "file5.cpp"]) 
subprocess.call("a",shell=True)