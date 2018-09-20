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
    parser.add_argument('dir_webcast', help='Diretório dos arquivos webcast')
    parser.add_argument('-p', '--probs_wu', type=int, metavar='N',
        help='Ajuste da quantidade de problemas removendo N problemas do warm-up',
        default=0)
    parser.add_argument('-j', '--janela', action='store_true',
        help='Apresenta o placar em uma janela')
    args = parser.parse_args()

    try:
        contest = Contest(args.dir_webcast)
        Handler.contest = contest
        contest.load_data(args.probs_wu)
        init_pygame(args.janela)
        handler = ScoreboardHandler()
    except InvalidWebcastError:
        print u'O webcast fornecido é inválido.'
        print u'Verifique se o URL foi digitado corretamente: %s' % (args.dir_webcast)
        exit(1)
    except IOError, e:
        print u'Não foi possível abrir o webcast: ' + e.strerror
        print u'Verifique se o URL foi digitado corretamente: %s' % (args.dir_webcast)
        exit(1)

    while 1:
        for event in pygame.event.get():
            handler.on_event(event)
        handler = handler.tick()

if __name__ == '__main__':
    main()
