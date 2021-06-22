import 'dart:convert' as convert;
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';
import 'package:process_run/shell.dart';

class User {
  String phone, name, ivrCode, token, identifier;

  User(this.phone, this.name, this.ivrCode, this.token, this.identifier);

  User.fromResponse(var response) {
    phone = response['phone'];
    name = response['last_name'];
    ivrCode = response['ivr_code'];
    token = response['token'];
    identifier = response['identifier'];
  }

  @override
  String toString() {
    return '$phone - $name - $ivrCode - $token - $identifier';
  }
}

Future<dynamic> postRequest(User user) async {
  var url = 'https://sentry.cordanths.com/Sentry/WebCheckin/Log';

  var body = <String, String>{
    'phone': user.phone,
    'last_name': user.name,
    'ivr_code': user.ivrCode,
    'lang': 'en'
  };
  final response = await http.post(url, body: body);
  return convert.jsonDecode(response.body);
}

void postTest(User user, bool testing, String msg) async {
  final today = DateTime.now();
  final formatter = DateFormat('yyyy-MM-dd');
  final formatted = formatter.format(today);
  // var url = 'https://drugnotify.herokuapp.com/tests/';
  var url = 'http://127.0.0.1:8000/tests/';

  var body = convert.jsonEncode({
    'user': user.identifier,
    'date_checked': formatted,
    'testing': testing,
    'message': msg,
  });
  final response = await http.post(url, body: body, headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  });
  return convert.jsonDecode(response.body);
}

Future<dynamic> getRequest() async {
  // var url = 'https://drugnotify.herokuapp.com/users/';
  var url = 'http://127.0.0.1:8000/users';

  final response = await http.get(url);
  return convert.jsonDecode(response.body);
}

Future<List> checkUser(User user) async {
  var shell = Shell();

  var response = await postRequest(user);
  var item = response[0];
  var msg = 'No Data';

  if (item['text'] != null) {
    msg = item['text'];
  } else {
    msg = response[0]['error_msg'];
  }

  var testing = msg.contains('required');
  var notificationMessage = (testing) ? 'Aw shit drink that water boii' : msg;

  await shell.run(
      './utils/push_notification_ios "${user.token}" "${user.name}" "$notificationMessage"');
  return [testing, msg];
}

Future<void> main(List<String> arguments) async {
  if (arguments.isNotEmpty) {
    print(arguments);
    var user = User(
        arguments[0], arguments[1], arguments[2], arguments[3], arguments[4]);
    await checkUser(user)
        .then((testing) => postTest(user, testing[0], testing[1]));
  } else {
    var response = await getRequest();

    for (var item in response) {
      var user = User.fromResponse(item);
      await checkUser(user)
          .then((testing) => postTest(user, testing[0], testing[1]));
    }
  }
}
