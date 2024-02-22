from py3pin.Pinterest import Pinterest
import json

class Py3PinterestWrapper:
    def __init__(self, email, password, username, cred_root, proxies=None):
        self.pinterest = Pinterest(email=email,
                                   password=password,
                                   username=username,
                                   cred_root=cred_root,
                                   proxies=proxies)

    def login(self, proxy=None):
        return self.pinterest.login(proxy=proxy)

    def logout(self):
        self.pinterest.logout()

    def get_user_profile(self):
        return self.pinterest.get_user_overview()

    def get_boards(self, username=''):
        return self.pinterest.boards(username=username)

    def get_board_feed(self, board_id):
        return self.pinterest.board_feed(board_id=board_id)

    def delete_pin(self, pin_id):
        return self.pinterest.delete_pin(pin_id=pin_id)

    def repin(self, board_id, pin_id):
        return self.pinterest.repin(board_id=board_id, pin_id=pin_id)

    def upload_pin(self, board_id, image_path, description, title, link='', section_id=None):
        return self.pinterest.upload_pin(board_id=board_id, 
                                         image_file=image_path, 
                                         description=description, 
                                         title=title, 
                                         link=link, 
                                         section_id=section_id)

    def get_pinnable_images(self, url):
        return self.pinterest.get_pinnable_images(url=url)

    def pin(self, board_id, image_url, description, title):
        return self.pinterest.pin(board_id=board_id, 
                                  image_url=image_url, 
                                  description=description, 
                                  title=title)

    def home_feed(self):
        return self.pinterest.home_feed()

    def board_recommendations(self, board_id):
        return self.pinterest.board_recommendations(board_id=board_id)

    def load_pin(self, pin_id):
        return self.pinterest.load_pin(pin_id=pin_id)

    def create_board_section(self, board_id, section_name):
        return self.pinterest.create_board_section(board_id=board_id, section_name=section_name)

    def delete_board_section(self, section_id):
        return self.pinterest.delete_board_section(section_id=section_id)

    def get_board_sections(self, board_id):
        return self.pinterest.get_board_sections(board_id=board_id)

    def follow_user(self, user_id=None, username=None):
        return self.pinterest.follow_user(user_id=user_id, username=username)

    def unfollow_user(self, user_id=None, username=None):
        return self.pinterest.unfollow_user(user_id=user_id, username=username)

    def get_following(self, username=''):
        return self.pinterest.get_following(username=username)

    def get_user_followers(self, username=''):
        return self.pinterest.get_user_followers(username=username)

    def follow_board(self, board_id):
        return self.pinterest.follow_board(board_id=board_id)

    def unfollow_board(self, board_id):
        return self.pinterest.unfollow_board(board_id=board_id)

    def search(self, scope, query):
        return self.pinterest.search(scope=scope, query=query)

    def visual_search(self, pin_data, x, y, w, h):
        return self.pinterest.visual_search(pin_data=pin_data, x=x, y=y, w=w, h=h)

    def invite_to_board(self, board_id, user_id):
        return self.pinterest.invite(board_id=board_id, user_id=user_id)

    def delete_invite(self, board_id, invited_user_id):
        return self.pinterest.delete_invite(board_id=board_id, invited_user_id=invited_user_id)

    def get_board_invites(self, board_id):
        return self.pinterest.get_board_invites(board_id=board_id)

    def comment(self, pin_id, text):
        return self.pinterest.comment(pin_id=pin_id, text=text)

    def delete_comment(self, pin_id, comment_id):
        return self.pinterest.delete_comment(pin_id=pin_id, comment_id=comment_id)

    def get_comments(self, pin_id):
        return self.pinterest.get_comments(pin_id=pin_id)

    def send_message(self, conversation_id, pin_id, message):
        return self.pinterest.send_message(conversation_id=conversation_id, pin_id=pin_id, message=message)

    def type_ahead(self, term):
        return self.pinterest.type_ahead(term=term)

# Example usage
if __name__ == "__main__":
  # Initialize wrapper with placeholders for your details
  pinterest_wrapper = Py3PinterestWrapper(email='your_email', password='your_password', username='your_username', cred_root='your_cred_root')

  # Login
  pinterest_wrapper.login()

  # Get user profile - uncomment to use
  # user_profile = pinterest_wrapper.get_user_profile()
  # print(user_profile)

  # Get boards - uncomment to use
  # boards = pinterest_wrapper.get_boards()
  # print(boards)

  # Create a pin - uncomment and replace placeholders
  # pin_response = pinterest_wrapper.upload_pin(board_id='your_board_id', image_path='path/to/image.png', description='Pin description', title='Pin title')
  # print(pin_response)

  # Get pinnable images from a URL - uncomment and replace URL
  # pinnable_images = pinterest_wrapper.get_pinnable_images(url='https://example.com')
  # print(pinnable_images)

  # Pin an image by URL - uncomment and replace placeholders
  # pin_by_url_response = pinterest_wrapper.pin(board_id='your_board_id', image_url='image_url', description='description', title='title')
  # print(pin_by_url_response)

  # Get home feed pins - uncomment to use
  # home_feed = pinterest_wrapper.home_feed()
  # print(home_feed)

  # Get board recommendations - uncomment and replace 'your_board_id'
  # recommendations = pinterest_wrapper.board_recommendations(board_id='your_board_id')
  # print(recommendations)

  # Load pin by ID - uncomment and replace 'pin_id'
  # pin_info = pinterest_wrapper.load_pin(pin_id='pin_id')
  # print(pin_info)

  # Follow a user - uncomment and replace 'target_user_id' or 'target_username'
  # follow_user_response = pinterest_wrapper.follow_user(user_id='target_user_id', username='target_username')
  # print(follow_user_response)

  # Search for boards with query 'food' - uncomment to use
  # search_results = pinterest_wrapper.search(scope='boards', query='food')
  # print(search_results)

  # Visual search - uncomment and replace placeholders
  # visual_search_response = pinterest_wrapper.visual_search(pin_data='pin_data', x=10, y=50, w=100, h=100)
  # print(visual_search_response)

  # Send a personal message - uncomment and replace placeholders
  # send_message_response = pinterest_wrapper.send_message(conversation_id='conversation_id', pin_id='pin_id', message='Your message here')
  # print(send_message_response)

  # Logout
  pinterest_wrapper.logout()

