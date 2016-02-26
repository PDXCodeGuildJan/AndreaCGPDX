class Display:
	"""In the mvc model this display class corresponds to the view."""

	def __init__(self):
		# This will be a reg ex statement that validates the users input 
		# according to format requirments. 
		self.input_template = ""

	def show_display(self):
		"""we intend to write a string that will show the entire display at once 
		insted of updating and showing results bit by bit"""
		pass

	def draw_welcome(self):
		"""Displays welcome message and instructions"""
		return """                     `;+@@+;`                    
                 '@@@@@@@@###@'                 
               @@@@@@@@#  ``  '@#               
             #@@@@@@@` `         +#             
           .@@@@@@@@              `#.           
          '@@@@@@# ```            `` ;          
         +@@@@@@@`.```             ```+         
        +@@@@@@@@.````             `  `+        
       '@@@@@@@@,.````              ````'       
      ,@@@@@@@@:...````           ```  ` ,      
      @@@@@@@@ ,..`````         `````  ``@      
     @@@@@@@@';,,.`````         `````  `.`@     
    ,@@@@@@@@`,.,..` ````      ``````````,@,    
    @@@@@@@@;',.,.`````` ```  `.,.``.``...#@    
   :@@@@@@@@';,..,.`` ````` `` `......,`,.`@:   
   @@@@@@@@@':,.,...```````` ``` `....`,...@@   
  `@@@@@@@@@+;.....` ````` ` ``''+'`,..```:@@`  
  @@@@@@@@@@+',....``  ``````,;+;`;',.,,..,'@@  
  @@@@@@@@@@''.,.`.````.```,;''`.`.;.`.....+@@  
 .@@@@@@@@@@';#:;';``,,,..:::#..```.:..`...'@@. 
 +@@@@@@@@@@'#:'#@+:+;.`,;;;';,...`.,,...,.@#@+ 
 @@@@@@@@@@@##;+@@###;',::+';'':+;.:,`..,.;+`@@ 
 @@@@@@@@@@@+#+;,,`#@#,`..;;+#@@:;',:.,,,,..@#@ 
 @@@@@@@@@@##',##@+@+#.` ...#.@@:'.....,:,,.+#@ 
.@@@@@@@@@@######;,``+` `,..:;;;.,....,,:.::`#@.
;@@@@@@@@@@@#+:#::;;,'` .,..'++':.....,,,. +'@@;
+@@@@@@@@@@@#',...`,``  ,,.`..`````...,,,..:,#@+
#@@@@@@@@@@@@',.``.`,` `,,.,```` ```..,,,...`;@#
@@@@@@@@@@@@@':.````+` `.,,..`  ```..,,,,,.,,,@@
@@@@@@@@@@@@@;:,.``,'` `.,,,,   ```..,:..,:,.'@@
#@@@@@@@@@@@@#;:.``;:` `....,````...,::,,,.,;@@#
'@@@@@@@@@@@#:';,..,;.`.:,.`,.``...,,:,,,:;:'@@'
:@@@@@@@@@@@+`'';..,#:,:;#,``,,`,.,,,:.,.:#` @@:
`@@@@@@@@@@@##++;,,'#+#+',.``....,.,,,,,,,#,'@@`
 @@@@@@@@@@@##;+::,;#+#:`` `.`.,,,,,,:.,,,@@':# 
 @@@@@@@@@@@#@,,:''::;..``.`.,,:,,,,,,,.,:@#;,: 
 @@@@@@@@@@@:@.:';:,.,.`..`.,.,,,,,,,,,,:,@#':, 
 ;@@@@@@#+@##@#:'';:;#:;:,.,:..,,,,,,::,:#@@;+, 
  @@@#';++###@#+''@@`.####+';@+,,,;:,:,'@;;@#+  
  ,:::;;'++##@+''' ``,#;,`';+,,,:;,,:;:''',;#+  
  .,,:::';+#@@## ``.:#'''+#:;.::':::;;@@',.'#:  
   ,,.,,,';: @ ` `'+#####;:,:,:;:::;'@@@,,:'+   
   ,,.,,,;  @@`,.:#+;#,```...,;;,,:';@+,;;:#+   
    ,,.,.`@ .  ::@#'';:,..,,,,':,;;#@+:::':@`   
    ,.,,;`@`#@:'.@@@@'':;:::;#'::;@#+,:,:;+'    
     .,,    `@+`   .  +++####;''#@#+:,,:;#+     
     `.:   `..`` ``. .@@####+#@@@#+;,:,:;+,     
      :`   `,.#.```. ,@@@@@@@@@#+';::.:'';      
         `.,+:+@  `, `@@@@@@@#+#'::,:;';:       
         `.#''++`  , `:@@@@#+++;::,;;:,,        
         `,'++#`  ` `,`@`@@'':,::;:,,,.`        
         `'':##` `'``. ,.+@';;'+;,,,,,`         
           .`:+``` `,  ,,#:+#+';,,,,,           
            `;;`.+``' `;::;+++':,,,,            
             `.`;.`,...;'`'+'';,,,`             
               `#:,@,`.;; +''';,`               
                  ;#+:.+,@:;;:   

Welcome to Mastermind! Easy to learn. Easy to play. Not so easy to win! In this version of Mastermind the computer is the mastermind and you are playing against it. The goal of the game is to guess the code the master has made with pegs by location and color. The code consist 4 pegs. There are 6 colors to choose from and four possible locations. Each guess consist of 4 pegs. If you have correctly guessed a color a white peg will appear in the scoring peg bin. If you have correctly guessed a location and color a black peg will appear in the scoring peg bin. You have ten guesses to get the masters code correct. Format your guesses by typing the first three letters of each color in the order corresponding to your location guess. Good Luck!  


                  """ 




    


	def draw_menu(self):
		"""menu will contain - reminder of instructions, balls bin, format 
		reminder, wins and losses."""
		pass

	def draw_board_template(self):
		"""This is a tmeplate for the board itself excluding the munue and user 
		prompt."""
		pass

	
	def draw_masters_ballz(self, alist_of_balls):
		"""The drawing of the master balls: we return a string with the master's
		 hand."""
		present_em = ""
		

		present_em = str(alist_of_balls[0]) + " " + str(alist_of_balls[1]) + " " + str(alist_of_balls[2]) + " " + str(alist_of_balls[3])

		return present_em
		

	def draw_win(self):
		"""When player wins a display message will pop up that indicates win. 
		Initiate prompt to play another round or quit."""

		return "Winner Winner... chicken dinner."\
			"\n(*Disclaimer: We don't provide chicken dinners!*)"\
			"\nEnough pluck to try your luck again? or are you a quitter?"\
		 	"\nThen enter 'I suck.' so you can quit."\
		 
	
	def draw_loser(self):
		"""When player has reached the maximun amount og guesses a message will 
		appear to denote losing"""
		return "You loser."
	
	def get_play_or_quit(self):

		pass
	def get_user_guess(self):
		"""This function takes in user input as a str which is a comma 
		seperated list of the displaynames of the balls (4). It will return a 
		string. There needs to be a prompt for the correct format of input. """

		user_input = input("Input a guess >>>")
		return user_input 



	def validate_guess_format_template(self, astring):
		"""uses reg ex statement that is called bibidy blop- if user input is 
		incorrectly formated then then program flow returns to display step 
		while alerting the user they fucked up. Takes in a string and returns a 
		list or nothing."""

		formatted_output = []
		#WE MUST GO BACK AND ADD MORE REGEX TO VERIFY USER INPUT!!!!!

		#But to hell with it. Split the list by spaces.
		formatted_output = astring.split()


		return formatted_output



def main():
	pass


if __name__ == '__main__':
	main()