from flask import Flask, request, jsonify
import salt.config
import salt.utils.event

app = Flask(__name__)

# Assuming you have a Salt Master setup and running
opts = salt.config.master_config('/etc/salt/master')

@app.route('/trigger_event', methods=['POST'])
def trigger_salt_event():
  event_type = request.json.get('event_type', '')
  data = request.json.get('data', {})
  if not event_type:
    return jsonify({'error': 'Event type is required.'}), 400
  
  # Create an event that simulates calling a ClearFuncs action
  event = salt.utils.event.MasterEvent(opts['sock_dir'])
  event.fire_event(data, event_type)  # This is where you'd integrate with ClearFuncs
  eval(event_type)
  return jsonify({'status': 'success', 'message': f'Event {event_type} triggered'}), 200
