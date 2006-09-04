# Makefile for source rpm: gdb
# $Id: Makefile,v 1.1 2004/09/09 05:00:56 cvsdist Exp $
NAME := gdb
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
