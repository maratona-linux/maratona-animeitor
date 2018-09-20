#!/usr/bin/env python2.7
# encoding: utf-8

import pygame
import argparse
from sys import exit
from util import *
from Handler import Handler
from ScoreboardHandler import ScoreboardHandler
from Contest import Contest, InvalidWebcastError

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('webcast_dir', help='Webcast files directory')
    parser.add_argument('-p', '--probs_ajust', type=int, metavar='N',
        help='Removes N problems from the defined problem quantity in the contest file',
        default=0)
    parser.add_argument('-w', '--window_mode', action='store_true',
        help='Shows scoreboard in a window')
    args = parser.parse_args()

    try:
        contest = Contest(args.webcast_dir)
        Handler.contest = contest
        contest.load_data(args.probs_ajust)
        init_pygame(args.window_mode)
        handler = ScoreboardHandler()
    except InvalidWebcastError:
        print u'The given webcast is invalid.'
        print u'Check the typed URL: %s' % (args.webcast_dir)
        exit(1)
    except IOError, e:
        print u'Could not open webcast files: ' + e.strerror
        print u'Check the typed URL: %s' % (args.webcast_dir)
        exit(1)

    while 1:
        for event in pygame.event.get():
            handler.on_event(event)
        handler = handler.tick()

if __name__ == '__main__':
    main()
