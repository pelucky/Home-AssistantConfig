DOMAIN = 'hello_event'

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    count = 0

    # Listener to handle fired events
    def handle_event(event):
        count += 1
        print('Total events received:', count)

    # Listen for when my_cool_event is fired
    hass.bus.listen('my_cool_event', handle_event)
