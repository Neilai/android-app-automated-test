import frida, sys
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
jscode = """
Java.perform(function ()
{
    var be= Java.use("curriculumActivity");
    send("start");
    be.getLecture.implementation = function()
    {
        send("send","函数getLecture调用");
        send("send","函数的参数是：");
        send("send",arguments);
       return true;

    };

});
"""
process = frida.get_usb_device().attach('cn.seu.herald_android.app_main')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Start...')
script.load()
sys.stdin.read()
