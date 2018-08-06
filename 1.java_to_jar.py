import os
jar_path = os.path.join(os.getcwd(), 'get_jar')
for file in os.listdir(jar_path):
    file_path = os.path.join(jar_path, filei)
    print('File_path:{}\n'.format(file_path))
    if '.java' in file:
        file_name = file[:-5]
        print('file_name: {}\n'.format(file_name))
        os.system('javac {}'.format(file_path))
    if '.class' in file:
        os.system('jar cvf {}.jar {}.class'.format())
