# Makefile for source rpm: gdb
# $Id$
NAME := gdb
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
