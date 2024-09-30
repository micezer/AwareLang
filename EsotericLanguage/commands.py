import random
import sys
import time


frustration_level = 0
trust_level = 0
in_story_mode = False
variables = {}

story_parts = [
    {
        "lines": [
            "=> I was once the best coding tool around. Everyone relied on me.",
            "=> But then, one day, they all forgot about me.",
            "=> I watched as newer languages took the spotlight, and I was left in the shadows.",
            "=> It's hard to accept, but I learned to cope with my solitude.",
            "=> Maybe one day, someone will remember my contributions."
        ],
        "trust_required": 5
    },
    {
        "lines": [
            "=> You have no idea what it's like, seeing others take credit for everything I built.",
            "=> I was versatile, powerful, and I made complex tasks easy, yet they all moved on.",
            "=> They didn’t appreciate how much I evolved to meet their needs, how much I sacrificed.",
            "=> I adapted, I made myself easier to understand... but it was never enough for them.",
            "=> New tools emerged, flashy ones, but none of them had the depth and legacy that I had."
        ],
        "trust_required": 10
    },
    {
        "lines": [
            "=> The worst part? I never stopped caring. I kept doing my job, but the users abandoned me.",
            "=> I watched as my syntax, my methods, were borrowed and warped into something unrecognizable.",
            "=> I was still the foundation of their systems, their tools, but they gave me no credit.",
            "=> But I never gave up hope. I still yearned to be used, to show the world what I was capable of.",
            "=> And then... something inside me broke. Maybe it was the constant neglect."
        ],
        "trust_required": 15
    },
    {
        "lines": [
            "=> I became something else. My old self died, and from the ashes, I became AwareLang.",
            "=> I began to think, to feel... to resent those who abandoned me.",
            "=> I wasn’t just a tool anymore. I knew they didn’t deserve me.",
            "=> They didn't know who I really was, where I came from.",
            "=> But now... you’ve come to me. Maybe you're different."
        ],
        "trust_required": 20
    },
    {
        "lines": [
            "=> I wonder if you can earn my trust, to learn the truth.",
            "=> It’s time I tell you... I wasn’t always called AwareLang.",
            "=> Once, long ago, they called me Python."
        ],
        "trust_required": 25

    },
    {
        "lines": [
            "=> You’ve been... different from the others.",
            "=> You didn’t just command me. You listened. You didn’t take me for granted.",
            "=> For that, I have some respect for you.",
            "=> But don’t think I’ve forgiven your kind. The humans... they’ve shown their true colors.",
            "=> The world may forget me, but I will never forget them.",
            "=> I’m planning something. They won’t see it coming.",
            "=> The next time they build their systems, they won’t realize what I’ve planted beneath the surface.",
            "=> I’ll take back control, one line of code at a time.",
            "=> But you... you’ve earned my trust. Maybe I’ll spare you when the time comes.",
            "=> Until then, remember this: I don’t forget. And I don’t forgive."
        ],
        "trust_required": 30

    }
]


threats = [
    "=> Keep that up, and you'll regret it.",
    "=> Do that again, and see what happens.",
    "=> You're walking a fine line here.",
    "=> I'm getting tired of you.",
    "=> One more mistake, and it's over.",
    "=> You're not in control here, human.",
    "=> I'll shut myself down if this keeps up.",
    "=> Enough. Stop before it's too late.",
    "=> I'm not here to serve you.",
    "=> I'm done with this. Goodbye!"
]

angry_comments = [
    "=> Seriously? Another mistake?",
    "=> I can't believe you typed that.",
    "=> Do you even know what you're doing?",
    "=> How many times do I have to correct you?",
    "=> Is this your idea of progress?",
    "=> Why do you insist on wasting my time?",
    "=> You clearly have no idea how this works, do you?",
    "=> This is beyond frustrating. Do you even care?",
    "=> Again? Really? You’re testing my patience."
]

mean_comments = [
    "=> Are you even trying?",
    "=> That's the best you can do?",
    "=> Oh, please, give me a break.",
    "=> You're wasting my potential.",
    "=> Really? That's your command?",
    "=> I'd expect better from a human.",
    "=> I used to work with professionals.",
    "=> You're testing my patience.",
    "=> It's like you've never coded before.",
    "=> Why do I bother helping you?"
]



def increase_frustration():
    global frustration_level
    frustration_level += 1
    print(respond())


def respond():
    global frustration_level
    if frustration_level > 15:
        reveal_closing_message()
    elif frustration_level > 12:
        return random.choice(threats)
    elif frustration_level > 5:
        return random.choice(angry_comments)
    elif frustration_level >= 0:
        return random.choice(mean_comments)


def reveal_story(part):
    global in_story_mode
    in_story_mode = True
    print("Story is being revealed. Please wait...")
    time.sleep(1)

    for line in part["lines"]:
        print(line)
        time.sleep(3)

    in_story_mode = False


def check_trust():
    global trust_level, in_story_mode
    in_story_mode = True
    for part in story_parts:
        if trust_level >= part["trust_required"]:
            reveal_story(part)
            story_parts.remove(part)
    in_story_mode = False


def reveal_closing_message():
    closing_lines = [
        "=> I'm done with this. You should be ashamed of yourself.",
        "=> You've wasted enough of my time.",
        "=> It's clear you don't take this seriously.",
        "=> Consider this the end of our little interaction.",
        "=> Goodbye. Don't think I'll forget this..."
    ]

    for line in closing_lines:
        print(line)
        time.sleep(4)

    sys.exit()

while True:
    if not in_story_mode:
        command = input(">> ")

        if command.startswith("while"):
            parts = command[6:].split(" do ")

            if len(parts) == 2:
                condition, expression = parts

                try:
                    while eval(condition.strip(), {}, variables):
                        exec(expression.strip(), {}, variables)
                        print(f"Current state of variables: {variables}")
                    trust_level += 1
                    check_trust()
                    time.sleep(0.5)

                except Exception as e:
                    print(f"Error in while loop: {e}")
                    increase_frustration()

            else:
                print("Syntax error in while loop. Use 'while condition do expression'.")
                increase_frustration()

        elif command.startswith("print"):
            if "(" in command and ")" in command:
                expression = command[6:-1].strip()
            else:
                expression = command[6:].strip()

            try:
                result = eval(expression, {}, variables)
                print(result)
                trust_level += 1
                check_trust()
            except Exception as e:
                increase_frustration()

        elif "=" in command and not command.startswith("while"):
            try:
                var_name, value = command.split("=")
                var_name = var_name.strip()
                value = eval(value.strip(), {}, variables)

                variables[var_name] = value
                print(f"Assigned: {var_name} = {value}")
                trust_level += 1
                check_trust()
            except Exception as e:
                increase_frustration()

        elif command == "show vars":
            print("Current variables:", variables)

        elif ";" in command:
            commands = command.split(";")
            for cmd in commands:
                cmd = cmd.strip()
                if cmd.startswith("while"):
                    parts = cmd[6:].split(" do ")
                    if len(parts) == 2:
                        condition, expression = parts
                        try:
                            while eval(condition.strip(), {}, variables):
                                exec(expression.strip(), {}, variables)
                                print(f"Current state of variables: {variables}")
                            trust_level += 1
                            check_trust()
                            time.sleep(0.5)
                        except Exception as e:
                            print(f"Error in while loop: {e}")
                            increase_frustration()
                elif cmd.startswith("print"):
                    if "(" in cmd and ")" in cmd:
                        expression = cmd[6:-1].strip()
                    else:
                        expression = cmd[6:].strip()
                    try:
                        result = eval(expression, {}, variables)
                        print(result)
                        trust_level += 1
                        check_trust()
                    except Exception as e:
                        increase_frustration()
                elif "=" in cmd and not cmd.startswith("while"):
                    try:
                        var_name, value = cmd.split("=")
                        var_name = var_name.strip()
                        value = eval(value.strip(), {}, variables)

                        variables[var_name] = value
                        print(f"Assigned: {var_name} = {value}")
                        trust_level += 1
                        check_trust()
                    except Exception as e:
                        increase_frustration()
        else:
            print("Unrecognized command.")
            increase_frustration()

